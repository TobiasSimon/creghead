#!/usr/bin/env python

# File: creghead.py
# Purpose: Import Python register/bits definition file and outputs c header to stdout
# Author: Tobias Simon, Ilmenau University of Technology
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA



import sys
import os


def import_file(full_path_to_module):
    try:
        module_dir, module_file = os.path.split(full_path_to_module)
        module_name, module_ext = os.path.splitext(module_file)
        sys.path.append(module_dir)
        module = __import__(module_name)
        return module
    except:
        raise ImportError


assert len(sys.argv) == 2
c = import_file(sys.argv[1])

def single_bit_output(define_prefix, name, bit_pos):
   print define_prefix + '_' + name + ' \\\n   (1 << (' + str(bit_pos) + '))'
   print define_prefix + '_GET_' + name + '(x) \\\n   (((x) >> ' + str(bit_pos) + ') & 1)'
   print define_prefix + '_SET_' + name + '(x) \\\n   do {x |= 1 << ' + str(bit_pos) + ';} while (0)'
   print define_prefix + '_CLEAR_' + name + '(x) \\\n   do {x &= ~(1 << ' + str(bit_pos) + ');} while (0)'

header = '''
/* 
 * AUTOGENERATED FILE - DO NOT EDIT!
 * file generated using creghead: https://github.com/TobiasSimon/creghead
 */

'''
print header
print '#ifndef __' + c.prefix + '_REGS_H__'
print '#define __' + c.prefix + '_REGS_H__'
for reg in c.regs:
   print '\n\n'
   try:
      reg_name, id, width, doc, bits = reg
      print '/* ' + doc + ' */'
   except:
      try:
         reg_name, id, width, bits = reg
      except:
         reg_name, id, width = reg
         bits = []
   define_prefix = '#define ' + c.prefix + '_' + reg_name
   print define_prefix + ' (' + hex(id) + ')'
   bit_pos = 0
   dbg_list = []
   for bit in bits:
      if not bit: # single unused bit
         print '/* bit ' + str(bit_pos) + ' ignored */'
         bit_pos += 1
      elif isinstance(bit, str): # undocumented 
         dbg_list.append((bit, c.prefix + '_' + reg_name + '_GET_' + bit + '(x)'))
         single_bit_output(define_prefix, bit, bit_pos)
         bit_pos += 1
      elif isinstance(bit, tuple):
         if bit[0]:
            if isinstance(bit[1], str):
               print '/* ' + bit[1] + ' */'
               dbg_list.append((bit[0], c.prefix + '_' + reg_name + '_GET_' + bit[0] + '(x)'))
               single_bit_output(define_prefix, bit[0], bit_pos)
               bit_pos += 1
            else:
               if len(bit) == 3:
                  print '/* ' + bit[2] + ' */'
               mask = hex(2 ** (bit[1]) - 1)
               dbg_list.append((bit[0], c.prefix + '_' + reg_name + '_GET_' + bit[0] + '(x)'))
               print define_prefix + '_GET_' + bit[0] + '(x) \\\n   (((x) >> ' + str(bit_pos) + ') & ' + mask + ')'
               print define_prefix + '_SET_' + bit[0] + '(x, v) \\\n   do {x &= ~(' + mask + ' << ' + \
                  str(bit_pos) + '); x |= (v & ' + mask + ') << ' + str(bit_pos) + ';} while(0)'
               bit_pos += bit[1]
         else:
            print '/* bits ' + str(bit_pos) + ' - ' + str(bit_pos + bit[1] - 1) + ' ignored */'
            bit_pos += bit[1]
      print
   if len(bits) > 0:
      print define_prefix + '_DEBUG(x) \\\n   do { printf("' + reg_name + ': ' +  ' = %X, "\\\n      "'.join(zip(*dbg_list)[0]) + \
            ' = %X\\n", ' + ', \\\n      '.join(zip(*dbg_list)[1]) + '); } while(0)'
      if bit_pos != width:
         raise AssertionError('final bit position %d does not match register width %d' % (bit_pos, width))
print '\n#endif /* __' + c.prefix + '_REGS_H__ */\n'

