from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
from itertools import product
from numba import jit
from time import time
import typer

app = typer.Typer()

@jit(target_backend="cuda")
def generator(char: str, columns: int, bookname: str):
    with open(bookname, 'w') as wordlist:
        for word in product(char, repeat=columns):
            print("".join(word), file=wordlist)

@app.command()
def ngin(chars: str, column: int, book_name: str):
    
    charecters = {
        1: ascii_letters,
        2: ascii_uppercase,
        3: ascii_lowercase,
        4: digits,
        5: punctuation,
    }

    if chars == "ABCDabcd":
        loop = time()
        generator(charecters[1], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "ABCD":
        loop = time()
        generator(charecters[2], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "abcd":
        loop = time()
        generator(charecters[3], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "1234":
        loop = time()
        generator(charecters[4], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "punch":
        loop = time()
        generator(charecters[5], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "ABCDabcd1234":
        loop = time()
        generator(charecters[1] + charecters[4], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "ABCD1234":
        loop = time()
        generator(charecters[2] + charecters[4], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "abcd1234":
        loop = time()
        generator(charecters[3] + charecters[4], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "ABCDpunch":
        loop = time()
        generator(charecters[1] + charecters[5], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "abcdpunch":
        loop = time()
        generator(charecters[3] + charecters[5], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "1234punch":
        loop = time()
        generator(charecters[4] + charecters[5], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    elif chars == "all":
        loop = time()
        generator(charecters[1] + charecters[4] + charecters[5], column, book_name)
        print(f"Completed in: {time() - loop}")
    
    else:
        print("Wrong input")

if __name__ == "__main__":
    app()