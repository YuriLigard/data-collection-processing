

class Content:
    
    def printing(self, nameMovie: str, infoMovie: str) -> str:
        Synopsis, link = infoMovie.split(">>")
        print(f"""
              \033[1mTítulo do Filme:\033[0m {nameMovie}
              \033[1mResumo:\033[0m {Synopsis}
              \033[1mOnde Posso Assistir:\033[0m {link}\n
            """)

