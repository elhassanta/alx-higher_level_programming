#include <listobject.h>
#include <object.h>

/**
* print_python_list_info - Prints basic info about Python lists.
* @p: PyObject list.
*/
void print_python_list_info(PyObject *p)
{
	int size, count, allocated;
	PyObject *object;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (count = 0; count < size; count++)
	{
		printf("Element %d: ", count);
		object = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
