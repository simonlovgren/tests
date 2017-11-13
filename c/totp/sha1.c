#include "sha1.h"

// Debug flag
#define DEBUG 0

// Define values needed for calculation
#define H0 0x67452301
#define H1 0xEFCDAB89
#define H2 0x98BADCFE
#define H3 0x10325476
#define H4 0xC3D2E1F0

// Macros
#define getbyte_0(data) (((uint64_t)data & 0x00000000000000FF))
#define getbyte_1(data) (((uint64_t)data & 0x000000000000FF00) >> 8)
#define getbyte_2(data) (((uint64_t)data & 0x0000000000FF0000) >> 16)
#define getbyte_3(data) (((uint64_t)data & 0x00000000FF000000) >> 24)
#define getbyte_4(data) (((uint64_t)data & 0x000000FF00000000) >> 32)
#define getbyte_5(data) (((uint64_t)data & 0x0000FF0000000000) >> 40)
#define getbyte_6(data) (((uint64_t)data & 0x00FF000000000000) >> 48)
#define getbyte_7(data) (((uint64_t)data & 0xFF00000000000000) >> 56)

char *sha1(char *msg, int64_t len) {
  // Size of message in bits
  int64_t orig_bits = len * sizeof(char) * 8;
  int64_t msg_bits = orig_bits;

  #if DEBUG
  printf("Message length: %lld bits\n", orig_bits);
  #endif

  // Append bit 1 to message by 0x80
  msg_bits += 8;
  
  // Calculate- and append padding needed to message
  int zeroes = 512 - ((msg_bits + 64) % 512);
  msg_bits += zeroes;
  
  #if DEBUG
  printf("Zero padding: %d bits\n", zeroes);
  #endif

  // Append 64 bit BIG ENDIAN 64-bit integer of orig_size
  msg_bits += 64;
  
  #if DEBUG
  printf("New size: %lld bits\n", msg_bits);
  #endif
  
  // allocate space for message length + 1 chars
  char * data = calloc(msg_bits >> 3, 1);

  // INSERT DATA
  int64_t offset = 0;

  // Copy original message
  offset += len * sizeof(char);
  memcpy((void *) data, (void *) msg, offset);

  // Insert bit 1 to correct position of array
  *(data + offset) = 0x80;
  offset += 1;

  // Skip to end of zeroes
  offset += zeroes >> 3;

  // Insert original size as big endian integer
  #if DEBUG
  orig_bits = 0x8899AABBCCDDEEFF;
  //printf("MSbyte: %02hhX\n", (int8_t)((char *)&orig_bits)[1]);
  printf("MSbyte: %02hhX\n", (int8_t)getbyte_7(orig_bits));
  printf("Byte 2: %02hhX\n", (int8_t)getbyte_6(orig_bits));
  printf("Byte 3: %02hhX\n", (int8_t)getbyte_5(orig_bits));
  printf("Byte 4: %02hhX\n", (int8_t)getbyte_4(orig_bits));
  printf("Byte 5: %02hhX\n", (int8_t)getbyte_3(orig_bits));
  printf("Byte 6: %02hhX\n", (int8_t)getbyte_2(orig_bits));
  printf("Byte 7: %02hhX\n", (int8_t)getbyte_1(orig_bits));
  printf("LSbyte: %02hhX\n", (int8_t)getbyte_0(orig_bits));
  printf("Offset: %llu\n", offset);
  #endif
  
  if (len > 0){
    // TODO: Make diz perdy yo! loop it or some shit
    *(data+offset) = getbyte_7(orig_bits);
    ++offset;
    *(data+offset) = getbyte_6(orig_bits);
    ++offset;
    *(data+offset) = getbyte_5(orig_bits);
    ++offset;
    *(data+offset) = getbyte_4(orig_bits);
    ++offset;
    *(data+offset) = getbyte_3(orig_bits);
    ++offset;
    *(data+offset) = getbyte_2(orig_bits);
    ++offset;
    *(data+offset) = getbyte_1(orig_bits);
    ++offset;
    *(data+offset) = getbyte_0(orig_bits);
    ++offset;
  }

  #if DEBUG
  printf("Offset: %llu\n", offset);

  puts("");
  for(int i = 1; i <= offset; ++i) {
    printf("%02hhX ", *(data + i - 1));
    if(i % 16 == 0) {
      puts("");
    }
  }
  #endif
  
  free(data);

  return "";
}
