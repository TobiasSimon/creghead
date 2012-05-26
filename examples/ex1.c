

#include "regs_ex1.h"
#include <stdio.h>
#include <stdint.h>


int main(void)
{
   uint16_t val = 0xFFFF;
   printf("val = %X\n", val);
   EXAMPLE_BUFFER_SET_RX_COUNT(val, 3);
   EXAMPLE_BUFFER_SET_TX_COUNT(val, 6);
   printf("val = %X\n", val);
   printf("rx-count: %d, tx-count: %d\n",
          EXAMPLE_BUFFER_GET_RX_COUNT(val),
          EXAMPLE_BUFFER_GET_TX_COUNT(val));
   printf("tx-error? %d\n", EXAMPLE_BUFFER_GET_TX_ERROR(val));
   EXAMPLE_BUFFER_CLEAR_TX_ERROR(val);
   printf("val = %X\n", val);
   printf("tx-error? %d\n", EXAMPLE_BUFFER_GET_TX_ERROR(val));
}

