import random
import time

from models.node import Virsotne
from models.game_tree import Speles_koks

from logic.tree_builder import uzgeneret_koku_no_virsotnes
from logic.minimax import izveleties_labako_gajienu as minimax_move, noteikt_dalitaju
from logic.alpha_beta import izveleties_labako_gajienu as alphabeta_move
from logic.heuristic import nav_gajienu


def parbuvet_koku_no_current(current):
    sp = Speles_koks()

    sakuma_virsotne = Virsotne(
        "A1",
        current.skaitlis,
        current.p1,
        current.p2,
        current.banka,
        1,
        current.gajiens
    )

    uzgeneret_koku_no_virsotnes(sp, sakuma_virsotne)
    virsotnes_dict = {v.id: v for v in sp.virsotnu_kopa}

    return sp, virsotnes_dict, sakuma_virsotne


def main():
    print("TESTA SPĒLE\n")

    alg = input("Izvēlies algoritmu (1 - minimax, 2 - alphabeta): ").strip()
    while alg not in ["1", "2"]:
        alg = input("Nepareiza izvēle. Ievadi 1 vai 2: ").strip()

    first = input("Kas sāk? (1 - cilvēks, 2 - dators): ").strip()
    while first not in ["1", "2"]:
        first = input("Nepareiza izvēle. Ievadi 1 vai 2: ").strip()

    skaitli = []
    while len(skaitli) < 5:
        x = random.randint(1000000, 5000000)
        if x % 216 == 0:
            skaitli.append(x)

    print("Sākuma skaitlis:", skaitli[0])

    sp = Speles_koks()

    sakuma_virsotne = Virsotne(
        "A1",
        skaitli[0],
        0,
        0,
        0,
        1,
        int(first)
    )

    current = sakuma_virsotne
    sp, virsotnes_dict, current_koka = parbuvet_koku_no_current(current)

    while True:
        print("\n-----------------------")
        print("Skaitlis:", current.skaitlis)
        print("Cilvēks:", current.p1)
        print("Dators:", current.p2)
        print("Banka:", current.banka)

        # spēles beigas
        if current.skaitlis == 2 or current.skaitlis == 3 or nav_gajienu(current):
            print("\nSpēle beigusies!")
            break

        sp, virsotnes_dict, current_koka = parbuvet_koku_no_current(current)

        # cilvēka gājiens
        if current.gajiens == 1:
            print("Tagad gājiens: cilvēks")

            while True:
                move_input = input("Tavs gājiens (2 vai 3): ").strip()

                if move_input not in ["2", "3"]:
                    print("Nepareiza ievade. Jāievada 2 vai 3.")
                    continue

                move = int(move_input)

                if current.skaitlis % move != 0:
                    print(f"Skaitli {current.skaitlis} nevar dalīt ar {move}. Izvēlies citu gājienu.")
                    continue

                next_number = current.skaitlis // move

                nakama_virsotne = None
                bernu_id = sp.loku_kopa.get(current_koka.id, [])

                for child_id in bernu_id:
                    v = virsotnes_dict[child_id]
                    if v.skaitlis == next_number:
                        nakama_virsotne = v
                        break

                if nakama_virsotne is None:
                    print("Šāds gājiens kokā netika atrasts. Izvēlies citu gājienu.")
                    continue

                print(f"Cilvēks izvēlējās dalīt ar {move}.")
                current = nakama_virsotne
                break

        # datora gājiens
        else:
            print("Tagad gājiens: dators")
            print("Dators domā", end="", flush=True)

            for _ in range(3):
                time.sleep(0.75)
                print(".", end="", flush=True)
            
            print()
            time.sleep(1)

            if alg == "1":
                move, value = minimax_move(current_koka, sp, virsotnes_dict)
            else:
                move, value = alphabeta_move(current_koka, sp, virsotnes_dict)

            if move is None:
                print("Datoram nav iespējamu gājienu.")
                break

            dalitajs = noteikt_dalitaju(current_koka, move)

            if dalitajs is not None:
                print(f"Dators izvēlējās dalīt ar {dalitajs}.")
            else:
                print(f"Dators izvēlējās pāreju uz {move.skaitlis}.")

            print(f"Heiristiskā vērtība: {value}")
            current = move

    print("\nRezultāts:")
    print("Cilvēks:", current.p1)
    print("Dators:", current.p2)


if __name__ == "__main__":
    main()