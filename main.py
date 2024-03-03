import pyautogui
import time


def press_key(key, duration=0):
    """Pressiona uma tecla por um determinado período de tempo."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)


def select_enemy():
    """Seleciona o inimigo pressionando 'Tab'."""
    pyautogui.press('tab')
    time.sleep(1)  # Espera 1 segundo para selecionar o inimigo


def attack():
    """Ataca o inimigo pressionando 'F1'."""
    pyautogui.press('f1')


def use_skill(skill_key):
    """Usa uma habilidade pressionando a tecla correspondente."""
    pyautogui.press(skill_key)


def use_potion(potion_key):
    """Usa uma poção pressionando a tecla correspondente."""
    pyautogui.press(potion_key)


def main():
    last_potion_time = time.time()  # Marca o tempo da última vez que a poção foi usada
    potion_key = '7'  # Tecla correspondente à poção de vida
    skill_key = '1'  # Tecla correspondente à habilidade

    while True:
        select_enemy()
        attack()
        for _ in range(3):  # Usa a habilidade 3 vezes
            use_skill(skill_key)
            time.sleep(1)  # Espera 1 segundo antes de usar a habilidade novamente

        # Verifica se é hora de usar a poção de vida (a cada 30 minutos)
        if time.time() - last_potion_time >= 30 * 60:
            use_potion(potion_key)
            last_potion_time = time.time()  # Atualiza o tempo da última vez que a poção foi usada


if __name__ == "__main__":
    main()
