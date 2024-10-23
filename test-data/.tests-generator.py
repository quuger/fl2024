import os
import itertools
import shutil


def generate_words(alphabet, max_words):
    words = []
    length = 1
    while len(words) < max_words:
        for word in itertools.product(alphabet, repeat=length):
            words.append(''.join(word))
            if len(words) >= max_words:
                break
        length += 1
    return words


def save_words_to_files(input_string, words, output_dir='tests'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, word in enumerate(words, 1):
        filename = os.path.join(output_dir, f"{idx:03}.txt")
        with open(filename, 'w') as file:
            file.write(f"{input_string}\n{word}\n")


def copy_directory(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)


def main():
    input_string = input()
    x = input()
    alphabet = sorted(set(c for c in input_string if c.islower()))
    max_words = 128
    words = generate_words(alphabet, max_words)

    tests_dir = 'tests'
    save_words_to_files(input_string, words, tests_dir)
    dest_dir = f"t{x}"
    copy_directory(tests_dir, os.path.join(dest_dir, tests_dir))


if __name__ == "__main__":
    main()
