path_makefile = '/home/slash/Software/makefiles/GNUmakefile'


import sys
import os
import logging
import shutil
PATH_DIR = os.getcwd()
#on gère le makefile
list_files = list()
for name in os.listdir(PATH_DIR):
    if os.path.isfile(os.path.join(PATH_DIR, name)):
        list_files.append(name)
if not 'GNUmakefile' in list_files:
	shutil.copy(path_makefile,os.path.join(PATH_DIR, 'GNUmakefile'))

args = sys.argv[1:] #on enlève le nom du fichier python

#on met des secu quand même
if len(args)==0:
	logging.error(f"{len(args)} arguments where given, you must provide at least 2 arguments")
	sys.exit()
for header_name in args[1:]:
	
	if os.path.exists(os.path.join(PATH_DIR, header_name.join(['','.h']))):
		logging.error(f"{os.path.join(PATH_DIR, header_name.join(['','.h']))} is already existing, please delete it or move it to another directory")
		sys.exit()
	if os.path.exists(os.path.join(PATH_DIR, header_name.join(['','.c']))):
		logging.error(f"{os.path.join(PATH_DIR, header_name.join(['','.c']))} is already existing, please delete it or move it to another directory")
		sys.exit()


#on choisi le mode
if os.path.exists(args[0]):
	include_headers = str()
	file_content = str()
	for header_name in args[1:]:
		include_headers += f"#include \"{header_name.join(['','.h'])}\"\n"
	with open(args[0],'r') as f:
		file_content = f.read()
	with open(args[0],'w') as f:
		f.write(include_headers + file_content)
	for header_name in args[1:]:
		with open(header_name.join(['','.h']), 'w') as f:
			f.write(f"#ifndef {header_name.join(['','_h']).upper()}\n#define {header_name.join(['','_h']).upper()}\n\n#endif")
		with open(header_name.join(['','.c']), 'w') as f:
			f.write(f"#include \"{header_name.join(['','.h'])}\"")

else: 
	#on s'occupe du fichier principal
	with open(args[0], 'w') as f:
		pass
		for header_name in args[1:]:
			f.write(f"#include \"{header_name.join(['','.h'])}\"\n")

		f.write(f"#include <stdio.h>\n\nint main(void)@\n\n     return 0;\n¨".replace('@','{').replace('¨','}')) #formatage de merde mais bon tant pis ça marche
	#au tour des headers et des modules
	for header_name in args[1:]:
		with open(header_name.join(['','.h']), 'w') as f:
			f.write(f"#ifndef {header_name.join(['','_h']).upper()}\n#define {header_name.join(['','_h']).upper()}\n\n#endif")
		with open(header_name.join(['','.c']), 'w') as f:
			f.write(f"#include \"{header_name.join(['','.h'])}\"")