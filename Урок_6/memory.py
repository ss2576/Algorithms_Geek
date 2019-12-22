import sys
import platform


def memory(f):
	memory_sum = 0
	print('*' * 80)
	for key, value in f.items():
		memory_sum += sys.getsizeof(value)
		print(f'переменная -{key}- имеет тип {type(value)} и занимает {sys.getsizeof(value)} байт')
	print(f'ОБЩАЯ СУММА ЗАНИМАЕМОЙ ПАМЯТИ : {memory_sum} байт')

def version():
	print('#'*25, 'Разрядность ОС и версия Python','#'*25 )
	print(platform.architecture())
	print(sys.version_info)