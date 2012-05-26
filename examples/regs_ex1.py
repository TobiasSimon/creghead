
prefix = 'EXAMPLE'
regs = [
   ('BUFFER', 0x00, 16, 'buffer status register',
      [
         ('RX_COUNT',   6, 'rx_buffered'),
         ('TX_COUNT',   6, 'tx_buffered'),
         (None,  2),   # 2 bits unused/reserved
         ('TX_ERROR',  'set when a tx error occured'),
         ('RX_EMPTY',  'GPS relative position transmission')
      ]
   ),
]

