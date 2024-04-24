con <- DBI::dbConnect(duckdb::duckdb(), dbdir = "my-db.duckdb")
DBI::dbWriteTable(con, "penguins", palmerpenguins::penguins, append = TRUE)
DBI::dbDisconnect(con)

