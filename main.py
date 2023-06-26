"""
Tool for merging text files into one file.

Usage:
python main.py --output_path=results/merged.txt --input_path=data/file* --remove-empty-lines

Options:
    --input-path=<input_path>
    --output-path<output_path> Default: merged.txt
    --remove-empty-lines Default:False

"""

import fnmatch
import os
import sys

print(sys.argv)


def pars_arguments_input_path(arguments: list[str]) -> str:
    """Parses input path from arguments."""
    pass


def pars_arguments_output_path(arguments: list[str]) -> str:
    """Parses output path from arguments."""
    pass


def pars_arguments_remove_empty_lines(arguments: list[str]) -> str:
    """Parses from arguments."""
    pass


def get_absolute_file_paths(folder_name: str, filter: str) -> list[str]:
    absolute_paths = []
    for dirpath, _, filenames in os.walk(folder_name):
        for filename in filenames:
            if fnmatch.fnmatch(filename, filter):
                absolute_path = os.path.abspath(os.path.join(dirpath, filename))
                absolute_paths.append(absolute_path)
    return absolute_paths


def read_text_file_to_list(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_data = file.readlines()
        return file_data


def strip_new_line_characters(file_data: list[str]) -> list[str]:
    return [line.strip() for line in file_data]


def remove_empty_lines(file_data: list[str]) -> list[str]:
    return [line for line in file_data if line != ""]


def write_list_to_text(file_data: list[str], file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in file_data:
            file.write(line + "\n")


def split_inputh_path(input_path: str) -> tuple[str, str]:
    """Splits input path into folder path and filter"""
    # Input: data/reports/repo


def main():
    # Parse arguments
    input_path = pars_arguments_input_path(sys.argy)
    output_path = pars_arguments_output_path(sys.argv)
    remove_empty_lines = pars_arguments_remove_empty_lines(sys.argv)

    # Read files
    all_files_paths = get_absolute_file_paths(data_folder_name, filter_file_name)
    merged_list = []
    for path in all_files_paths:
        file_data = read_text_file_to_list(path)
        merged_list += file_data

    # Remove new line characters
    merged_list = strip_new_line_characters(merged_list)

    # Remove empty lines
    if remove_empty_lines:
        merged_list = remove_empty_lines(merged_list)

    # Write to file
    write_list_to_text(merged_list, final_merged_file)

    print("done!")
