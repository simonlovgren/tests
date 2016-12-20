#include <stdio.h>
#include <mysql.h>
#include <string.h>

int main(int argc, char *argv[])
{
  MYSQL *conn;
  MYSQL_RES *res;
  MYSQL_ROW row;
  char *host = "localhost";
  char *user = "root";
  char *password = "";
  char *database = "hotel";

  conn = mysql_init(NULL);

  // Connect to database
  if(!mysql_real_connect(conn, host, user, password, database, 0, NULL, 0))
    {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
    }

  // Create prepared statement
  char *sql = "SELECT EANHotelID, Name FROM Property WHERE PropertyCurrency = 'USD' AND HighRate = ?";
  MYSQL_STMT *stmt = mysql_stmt_init(conn);
  if(stmt == NULL && mysql_stmt_prepare(stmt, sql, strlen(sql)) != 0)
    {
      goto ERROR;
    }

  // 
  
  // Print result
  /* printf("\nTables in database %s:\n\n", database); */
  /* while((row = mysql_fetch_row(res)) != NULL) */
  /*   { */
  /*     printf("\t%s\n", row[0]); */
  /*   } */
  /* puts(""); */

  // Close connection
  mysql_free_result(res);
  mysql_close(conn);
  
  return 0;

 ERROR:
   // Close connection
  mysql_free_result(res);
  mysql_close(conn);
  return 1;
}
