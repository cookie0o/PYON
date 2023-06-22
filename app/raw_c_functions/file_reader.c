#include <stdio.h>
#include <stdlib.h>

// Function to read a file and return its contents
const char* read_file(const char* filepath) {
    FILE* file = fopen(filepath, "r");
    if (file == NULL) {
        printf("Failed to open file: %s\n", filepath);
        return NULL;
    }

    // Get the file size
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory to store the file contents
    char* buffer = (char*)malloc(file_size + 1);
    if (buffer == NULL) {
        printf("Memory allocation failed.\n");
        fclose(file);
        return NULL;
    }

    // Read the file contents
    size_t read_size = fread(buffer, 1, file_size, file);
    buffer[read_size] = '\0';

    fclose(file);
    return buffer;
}