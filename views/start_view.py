from colorama import Fore, Style, init

init(autoreset=True)

class StartView:
    def __init__(self) -> None:
        self.search_value = None

    def prompt_search(self) -> None:
        self.search_value = input(f"{Fore.CYAN}{Style.BRIGHT}Digite sua pesquisa: {Style.RESET_ALL}")

    def show_start(self) -> None:
        print(
            f"{Fore.MAGENTA}{Style.BRIGHT}[INFO]{Style.RESET_ALL} "
            f"Iniciando busca por: {Fore.CYAN}{self.search_value}{Style.RESET_ALL}"
        )

    def show_end(self) -> None:
        print(
            f"{Fore.GREEN}{Style.BRIGHT}[INFO]{Style.RESET_ALL} "
            f"Busca concluída para: {Fore.CYAN}{self.search_value}{Style.RESET_ALL}"
        )