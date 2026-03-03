from colorama import Fore, Style, init

init(autoreset=True)

class CheckerView:
    def __init__(self) -> None:
        self.url = None
        self.c_quantity = None
        self.status = False
        self.num_code = None
        self.start_routes = None

    def highsecurity_response(self, url, start_routes, status) -> None:
        self.url = url
        self.start_routes = start_routes
        self.status = status
        status_value = f"{Fore.GREEN}APROVADO!{Style.RESET_ALL}" if self.status else f"{Fore.RED}REPROVADO!{Style.RESET_ALL}"
        print(
            f"{Fore.GREEN}{Style.BRIGHT}[REQUEST SUCCESS]{Style.RESET_ALL} "
            f"{Fore.CYAN}{self.url}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.YELLOW}ROUTES FOUND: {self.start_routes}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.MAGENTA}STATUS: {status_value}{Style.RESET_ALL}"
        )

    def route_response(self, url, num_code, status) -> None:
        self.url = url
        self.num_code = num_code
        self.status = status
        status_value = f"{Fore.GREEN}APROVADO!{Style.RESET_ALL}" if self.status else f"{Fore.RED}REPROVADO!{Style.RESET_ALL}"
        print(
            f"{Fore.RED}{Style.BRIGHT}[ROUTE ERROR]{Style.RESET_ALL} "
            f"{Fore.CYAN}{self.url}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.YELLOW}HTTP CODE: {self.num_code}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.MAGENTA}STATUS: {status_value}{Style.RESET_ALL}"
        )

    def security_response(self, url, c_quantity, status) -> None:
        self.url = url
        self.c_quantity = c_quantity
        self.status = status
        status_value = f"{Fore.GREEN}APROVADO!{Style.RESET_ALL}" if self.status else f"{Fore.RED}REPROVADO!{Style.RESET_ALL}"
        severity_color = Fore.GREEN if self.status else Fore.RED
        print(
            f"{Fore.BLUE}{Style.BRIGHT}[SECURITY ALERT]{Style.RESET_ALL} "
            f"{Fore.CYAN}{self.url}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{Fore.YELLOW}DETECTIONS: {self.c_quantity}{Style.RESET_ALL} "
            f"{Fore.WHITE}|{Style.RESET_ALL} "
            f"{severity_color}{Style.BRIGHT}STATUS: {status_value}{Style.RESET_ALL}"
        )