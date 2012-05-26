
prefix = 'UM6'
regs = [
   ('COMM', 0x00, 32, 'communication settings',
      [
         ('BC_RATE',   8, 'packet broadcast frequency; freq = (280 / 255) * broadcast_rate + 20'),
         ('BAUD_RATE', 3, 'serial port baudrate; 000: 9600, 001: 14400, 010: 19200, 011 -> 38400, 100 -> 57600, 101 -> 115200'),
         ('GPS_BAUD',  3, 'GPS baudrate see BAUD_RATE for details'),
         None,
         ('SAT',  'detailed satellite status transmission'),
         ('SUM',  'satellite summary transmission'),
         ('VEL',  'GPS course and velocity transmission'),
         ('REL',  'GPS relative position transmission'),
         ('POS',  'GPS position transmission'),
         ('TEMP', 'temperature transmission'),
         ('COV',  'covariance matrix transmission'),
         ('EU',   'euler angles transmission'),
         ('QT',   'quaternion transmission'),
         ('MP',   'processed magnetometer transmission'),
         ('AP',   'processed accelerometer transmission'),
         ('GP',   'processed gyro transmission'),
         ('MR',   'raw magnetometer transmission'),
         ('AR',   'raw accelerometer transmission'),
         ('GR',   'raw gyro transmission'),
         ('BEN',  'broadcast mode'),
         None
      ]
   ),
]

