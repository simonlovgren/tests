
/**
 * Svenska översättning av C
 */


/**
 *  Macron
 */

// Datatyper -- funkar inte...
#define  kort       short
#define  lang       long
#define  signerad   signed
#define  signerat   signed
#define  osignerad  unsigned
#define  osignerat  unsigned

//#define  enum  enum
#define  konstant   const
//#define  extern  extern
//#define  register  register
#define  statisk    static
#define  inget      void
#define  struktur   struct
#define  typdef     typedef
#define  storlekav  sizeof

// Kontrollflöde
#define bryt break
#define gatill goto
#define fortsatt continue
#define om if
#define annars else
#define eller else if
#define gor   do
#define medan while
#define for   for
#define vaxla switch
#define fall  case
#define basfall default


// Nyckelord
// -- Funktioner
#define returnera      return
#define huvudfunktion  main
#define avsluta        exit



/**
 * Datatyper
 */
typedef char bokstav;
typedef int heltal;
typedef float decimaltal;
typedef double dubbel;



/**
 * stdio.h
 */
#if defined _STDIO_H || defined  _STDIO_H_

//#define stdin     stdin
#define stdut     stdout
#define stdfel    stderr
#define SPF       EOF
#define hamtab    getchar
#define skrivb    putchar
#define skrivf    printf
#define sskrivf   sprintf
#define lasf      scanf
#define slasf     sscanf
#define hamtas    gets
#define skrivs    puts
#define FIL       FILE
#define foppna    fopen
#define hamtasb   getc
#define skrivsb   putc
#define fskrivf   fprintf  
#define flasf     fscanf
#define fstang    fclose
#define ffel      ferror
#define fspf      feof
#define fhamtas   fgets
#define fskrivs   fputs

#endif


/**
 * ctype.h
 */
#if defined _CTYPE_H || defined _CTYPE_H_

#define aralnum(C)    isalnum(C) 
#define aralfa(C)     isalpha(C)
#define arkntrl(C)    iscntrl(C)
#define arsiffra(C)   isdigit(C)
#define argraf(C)     isgraph(C)
#define argemen(C)    islower(C)
#define arutskr(C)    isprint(C)
#define arpunkt(C)    ispunct(C)
#define arblank(C)    isspace(C)
#define arversal(C)   isupper(C)
#define arhexa(C)     isxdigit(C)
#define tillgemen(C)  tolower(C)
#define tillversal(C) toupper(C)

#endif

/**
 * string.h
 */
#if defined _STRING_H || defined _STRING_H_

#define strlan   strlen
#define strkop   strcpy
#define strnkop  strncpy
#define strkat   strcat
#define strnkat  strncat
#define strjmf   strcmp
#define strnjmf  strncmp
#define strbok   strchr
#define strsbok  strrchr
#define minkop   memcpy
#define minflytt memmove
#define minjmf   memcmp
#define minbok   memchr
#define minsatt  memset

#endif

/**
 * stdlib.h
 */
#if defined _STDLIB_H || defined _STDLIB_H_

//#define abs        abs
//#define labs       labs
//#define div        div
//#define ldiv       ldiv
#define slump      rand
#define gslump     srand
//#define system     system

#define atilld     atof
#define atillh     atoi
#define atilll     atol
#define strtilld   strtod
#define strtilll   strtol
#define strtillol  strtoul

#define allokera   malloc
#define nallokera  calloc
#define omallokera realloc
#define frigor     free

#define bsearch    bsok
#define ssort      qsort

#endif

/**
 * stdarg.h
 */
#if defined _STDARG_H || _STDARG_H_

//#define va_list va_list
//#define va_start va_start
//#define va_arg va_arg
#define va_slut va_end

#endif


/**
 * time.h
 */
#if defined _TIME_H || defined _TIME_H_

#define klocka   clock
#define tid      time
#define difftid  difftime
#define sktid    mktime
#define strtid   asctime
#define ktid     ctime
#define gmtid    gmtime
#define lokaltid localtime
#define strftid  strftime

typedef clock_t klocka_t;
typedef time_t tid_t;
//tm
//tm_sec
//tm_min
//tm_hour
//tm_mday
//tm_mon
//tm_year
//tm_wday
//tm_yday
//tm_isdst

#endif

/**
 * math.h
 */
#if defined _MATH_H || defined _MATH_H_ || defined __MATH__

//#define sin
//#define cos
//#define tan
//#define asin
//#define acos
//#define atan
//#define atan2
//#define sinh
//#define cosh
//#define tanh
//#define exp
//#define log
//#define log10
//#define ldexp
//#define frexp
//#define modf
//#define fmod
#define upph pow
#define kvdr sqrt
#define rundupp ceil
#define rundned floor
// #define fabs //??

#endif

/**
 * limits.h
 */
#if defined _LIMITS_H || defined _LIMITS_H_
const size_t BOKST_BIT = CHAR_BIT;
const size_t BOKST_MAX = CHAR_MAX;
const size_t BOKST_MIN = CHAR_MIN;
const size_t HELT_MAX = INT_MAX;
const size_t HELT_MIN = INT_MIN;
const size_t LANG_MAX = LONG_MAX;
const size_t LANG_MIN = LONG_MIN;
const size_t SBOKST_MAX = SCHAR_MAX;
const size_t SBOKST_MIN = SCHAR_MIN;
const size_t KORT_MAX = SHRT_MAX;
const size_t KORT_MIN = SHRT_MIN;
const size_t OBOKST_MAX = UCHAR_MAX;
const size_t OHELT_MAX = UINT_MAX;
const size_t OLANG_MAX = ULONG_MAX;
const size_t OKORT_MAX = USHRT_MAX;
#endif


/**
 * float.h
 */
