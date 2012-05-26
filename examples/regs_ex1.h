
/* 
 * AUTOGENERATED FILE - DO NOT EDIT!
 *
 */

#ifndef __EXAMPLE_REGS_H__
#define __EXAMPLE_REGS_H__

/* buffer status register */
#define EXAMPLE_BUFFER (0)
/* rx_buffered */
#define EXAMPLE_BUFFER_GET_RC_COUNT(x) \
   (((x) >> 0) & 0x3f)
#define EXAMPLE_BUFFER_SET_RC_COUNT(x, v) \
   do {x &= ~(0x3f << 0); x |= (v & 0x3f) << 0;} while(0)

/* tx_buffered */
#define EXAMPLE_BUFFER_GET_TX_COUNT(x) \
   (((x) >> 6) & 0x3f)
#define EXAMPLE_BUFFER_SET_TX_COUNT(x, v) \
   do {x &= ~(0x3f << 6); x |= (v & 0x3f) << 6;} while(0)

/* bit 12 ignored */

/* set when a tx error occured */
#define EXAMPLE_BUFFER_GET_TX_ERROR(x) \
   (((x) >> 14) & 1)
#define EXAMPLE_BUFFER_SET_TX_ERROR(x) \
   do {x |= 1 << 14;} while (0)
#define EXAMPLE_BUFFER_CLEAR_TX_ERROR(x) \
   do {x &= ~(1 << 14);} while (0)

/* GPS relative position transmission */
#define EXAMPLE_BUFFER_GET_RX_EMPTY(x) \
   (((x) >> 15) & 1)
#define EXAMPLE_BUFFER_SET_RX_EMPTY(x) \
   do {x |= 1 << 15;} while (0)
#define EXAMPLE_BUFFER_CLEAR_RX_EMPTY(x) \
   do {x &= ~(1 << 15);} while (0)

#endif /* __EXAMPLE_REGS_H__ */

