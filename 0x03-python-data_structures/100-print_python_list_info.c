#include <Python.h>
/**
* print_python_list_info - Prints basic info about Python lists.
* @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
{
	int alloc, size;
	PyObject *obj;
	siz = Py_SIZE(p);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
}
