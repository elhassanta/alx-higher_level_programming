#include <Python.h>

/**
* print_python_list_info - Prints basic info about Python lists.
* @p: PyObject list.
*/
void print_python_list_info(PyObject *p)
{
	int size, count;

	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	for (count = 0; count < size; count++)
	{
		printf("Element %d: ", count);
	}
}
