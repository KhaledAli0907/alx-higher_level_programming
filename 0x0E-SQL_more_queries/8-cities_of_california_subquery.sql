-- lists all the cities of California in the database hbtn_0d_usaSELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
	  ORDER BY id;
