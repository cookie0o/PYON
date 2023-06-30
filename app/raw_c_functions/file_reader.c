#include <Python.h>

static PyObject* read_file(PyObject* self, PyObject* args) {
    const char* filename;
    FILE* file;
    char buffer[4096];
    PyObject* result;

    if (!PyArg_ParseTuple(args, "s", &filename)) {
        return NULL;
    }

    file = fopen(filename, "r");
    if (file == NULL) {
        PyErr_SetString(PyExc_IOError, "Failed to open the file.");
        return NULL;
    }

    result = PyList_New(0);  // Create an empty list

    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        PyObject* line = PyUnicode_FromString(buffer);
        PyList_Append(result, line);  // Append each line to the list
        Py_DECREF(line);  // Decrement the reference count
    }

    fclose(file);
    return result;
}

static PyMethodDef methods[] = {
    {"read_file", read_file, METH_VARARGS, "Read a file and return its contents as a list."},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "file_reader",
    "Module to read a file",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_file_reader(void) {
    return PyModule_Create(&module);
}