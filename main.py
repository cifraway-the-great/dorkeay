from controllers.verify_controller import VerifyController
from views.start_view import StartView

class Start:
    def __init__(self) -> None:
        self.view = StartView()
        self.view.prompt_search()

    def search(self) -> None:
        self.view.show_start()
        sc = VerifyController(self.view.search_value)
        sc.find_domains()
        self.view.show_end()

if __name__ == "__main__":
    st = Start()
    st.search()