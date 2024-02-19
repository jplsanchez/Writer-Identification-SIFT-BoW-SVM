import os
import ast
from main import Keys
from src.logger import file_log
from helpers import average, error


def main():
    PATH = "../results/"
    for filename in [f for f in os.listdir(PATH) if f.endswith('.txt') and f != 'log.txt']:
        list_of_results = []
        print(filename)
        with open(PATH+"""\\"""+filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                print(f"{i+1}/{len(lines)}")
                list_of_results.append(ast.literal_eval(line))

        file_log(f"{{{Keys.NUM_OF_WRITERS}: \"{list_of_results[0][Keys.NUM_OF_WRITERS]}\", {Keys.VOCAB_SIZE}: \"{list_of_results[0][Keys.VOCAB_SIZE]}\", mean_{Keys.ACCURACY}: \"{average(Keys.ACCURACY, list_of_results)}\", mean_{Keys.TOTAL_TIME}: \"{average(Keys.TOTAL_TIME, list_of_results)}\", mean_{Keys.CODEBOOK_TIME}: \"{average(Keys.CODEBOOK_TIME, list_of_results)}\", mean_{Keys.SVM_TIME}: \"{average(Keys.SVM_TIME, list_of_results)}\", {Keys.NUM_OF_WRITERS}: \"{list_of_results[0][Keys.NUM_OF_WRITERS]}\", {Keys.VOCAB_SIZE}: \"{list_of_results[0][Keys.VOCAB_SIZE]}\", error_{Keys.ACCURACY}: \"{error(Keys.ACCURACY, list_of_results)}\", error_{Keys.TOTAL_TIME}: \"{error(Keys.TOTAL_TIME, list_of_results)}\", error_{Keys.CODEBOOK_TIME}: \"{error(Keys.CODEBOOK_TIME, list_of_results)}\", error_{Keys.SVM_TIME}: \"{error(Keys.SVM_TIME, list_of_results)}\"}},")


if __name__ == '__main__':
    main()
