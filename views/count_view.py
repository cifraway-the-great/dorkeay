from colorama import Fore, Style, init

init(autoreset=True)

class CountView:
    def __init__(self, websites) -> None:
        self.quantity_domains = len(websites)
        self.num_passed = None

    def count_domains(self) -> None:
        print(
            f"{Fore.MAGENTA}{Style.BRIGHT}[TOTAL DOMAINS]{Style.RESET_ALL} "
            f"{Fore.CYAN}{self.quantity_domains}{Style.RESET_ALL} "
            f"{Fore.WHITE}URLs disponíveis{Style.RESET_ALL}"
        )

    def count_passed(self, num_passed) -> None:
        self.num_passed = num_passed
        percent = (self.num_passed / self.quantity_domains) * 100 if self.quantity_domains > 0 else 0.0
        percent_str = f"{percent:.2f}%"
        print(
            f"{Fore.GREEN}{Style.BRIGHT}[PROCESS FINISHED]{Style.RESET_ALL} "
            f"{Fore.CYAN}Approved: {self.num_passed}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.YELLOW}Success Rate: {percent_str}{Style.RESET_ALL}"
        )