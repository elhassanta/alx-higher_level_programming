#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
* print_python_bytes - Prints bytes information
**
@p: Python Object
* Return: no return
*/
void print_python_bytes(PyObject *p)
{
char *str;
long int size, i, limit;
printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf(" [ERROR] Invalid Bytes Object\n");
return;
}
size = ((PyVarObject *)(p))->ob_size;
str = ((PyBytesObject *)p)->ob_sval;
printf(" size: %ld\n", size);
printf(" trying string: %s\n", str);
if (size >= 10)
limit = 10;
else
limit = size + 1;
printf(" first %ld bytes:", limit);
for (i = 0; i < limit; i++)
if (str[i] >= 0)
printf(" %02x", str[i]);
else
printf(" %02x", 256 + str[i]);
printf("\n");
}
