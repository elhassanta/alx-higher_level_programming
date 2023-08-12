#include <Python.h>
/**
* print_python_list_info - Prints basic info about Python lists.
* @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
{
	int alloc, size, count;
	PyObject *obj;

	siz = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (count = 0; count < size; count++)
	{
		printf("Element %d: ", count);
		obj = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
