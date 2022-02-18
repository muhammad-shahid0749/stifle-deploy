DELIMITER //
CREATE PROCEDURE OFAC_SDN_COMPARISION ()
  BEGIN
  DECLARE DATE_INSERTED_CURRENT VARCHAR(100);
  DECLARE DATE_INSERTED_PREVIOUS  VARCHAR(100);
  

	SET @DATE_INSERTED_CURRENT = (SELECT DATE_FORMAT(STR_TO_DATE(DATE_INSERTED, '%Y-%m-%d %H:%i'),'%Y-%m-%d %H:%i')   AS DATE_INSERTED 
				FROM ofac_sdn
				GROUP BY DATE_FORMAT(STR_TO_DATE(DATE_INSERTED, '%Y-%m-%d %H:%i'),'%Y-%m-%d %H:%i') 
				ORDER BY DATE_INSERTED DESC
				LIMIT 1);

	SET @DATE_INSERTED_PREVIOUS = (SELECT DATE_INSERTED 
				FROM (SELECT DATE_FORMAT(STR_TO_DATE(DATE_INSERTED, '%Y-%m-%d %H:%i'),'%Y-%m-%d %H:%i') AS DATE_INSERTED 
					FROM ofac_sdn 
					GROUP BY DATE_FORMAT(STR_TO_DATE(DATE_INSERTED, '%Y-%m-%d %H:%i'),'%Y-%m-%d %H:%i') 
					ORDER BY DATE_INSERTED DESC
					LIMIT 2) 
				AS ofac_sdn 
				ORDER BY DATE_INSERTED ASC 
				LIMIT 1);  
			
	DROP TEMPORARY TABLE IF EXISTS compliance.tmp_ofac_sdn;
  
	CREATE TEMPORARY TABLE compliance.tmp_ofac_sdn ( 
		DATAID VARCHAR(100) NOT NULL,
		FIRST_NAME VARCHAR(500),
		LAST_NAME VARCHAR(500),
		SDN_TYPE VARCHAR(100),
		REMARKS TEXT,
		PROGRAM_LIST VARCHAR(100),
		DATE_INSERTED VARCHAR(100) 
		);
  
	INSERT INTO compliance.tmp_ofac_sdn
	SELECT 
	 T1.DATAID, T1.FIRST_NAME, T1.LAST_NAME, T1.SDN_TYPE, T1.REMARKS, T1.PROGRAM_LIST, T1.DATE_INSERTED
	FROM ofac_sdn AS T1
		LEFT JOIN ofac_sdn AS T2 
		ON T1.DATAID = T2.DATAID  
		AND T2.DATE_INSERTED = @DATE_INSERTED_PREVIOUS 
	WHERE T1.DATE_INSERTED = @DATE_INSERTED_CURRENT
		AND IF(T2.DATAID IS NULL, TRUE, ((T1.FIRST_NAME <> T2.FIRST_NAME) 
		OR (T1.LAST_NAME <> T2.LAST_NAME)
		OR (T1.SDN_TYPE <> T2.SDN_TYPE) 
		OR (T1.REMARKS <> T2.REMARKS)
		OR (T1.PROGRAM_LIST <> T2.PROGRAM_LIST)));
		
	DROP TEMPORARY TABLE IF EXISTS compliance.tmp2_ofac_sdn;

	CREATE TEMPORARY TABLE compliance.tmp2_ofac_sdn ( 
		DATAID VARCHAR(100) NOT NULL,
		xmldoc TEXT
		);
		
	INSERT INTO compliance.tmp2_ofac_sdn
	SELECT
	   l.DATAID,
	   CONCAT('<DATAID DATA_ID="', l.DATAID, '">',
	    (
		SELECT
		    CONCAT('<DATA>',
		    GROUP_CONCAT('<FNP="', IFNULL(FirstName.PREVIOUS_FIRST_NAME, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<FNC="', IFNULL(FirstName.CURRENT_FIRST_NAME, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<LNP="', IFNULL(LastName.PREVIOUS_LAST_NAME, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<LNC="', IFNULL(LastName.CURRENT_LAST_NAME, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<SDN_TYPEP="', IFNULL(SDN_TYPE1.PREVIOUS_SDN_TYPE, 'NULL'),  '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<SDN_TYPEC="', IFNULL(SDN_TYPE1.CURRENT_SDN_TYPE, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<REMARKSP="', IFNULL(REMARKS1.PREVIOUS_REMARKS, 'NULL'),  '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<REMARKSC="', IFNULL(REMARKS1.CURRENT_REMARKS, 'NULL'), '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<PROGRAM_LISTP="', IFNULL(PROGRAM_LIST1.PREVIOUS_PROGRAM_LIST, 'NULL'),  '"/>'  SEPARATOR ''),
		    GROUP_CONCAT('<PROGRAM_LISTC="', IFNULL(PROGRAM_LIST1.CURRENT_PROGRAM_LIST, 'NULL'), '"/>'  SEPARATOR ''),
		    '</DATA>')
	    FROM(
		(SELECT pre.DATAID,
		    pre.FIRST_NAME AS PREVIOUS_FIRST_NAME,
		    cur.FIRST_NAME AS CURRENT_FIRST_NAME
		FROM ofac_sdn pre
		    LEFT JOIN ofac_sdn cur
		    ON cur.DATAID = pre.DATAID
		    AND cur.DATE_INSERTED = @DATE_INSERTED_CURRENT
		WHERE NOT (pre.FIRST_NAME <=> cur.FIRST_NAME) AND pre.DATE_INSERTED = @DATE_INSERTED_PREVIOUS) AS FirstName

		LEFT JOIN (
		SELECT pre.DATAID,
		    pre.LAST_NAME AS PREVIOUS_LAST_NAME,
		    cur.LAST_NAME AS CURRENT_LAST_NAME
		FROM ofac_sdn pre
		    LEFT JOIN ofac_sdn cur
		    ON cur.DATAID = pre.DATAID
		    AND cur.DATE_INSERTED = @DATE_INSERTED_CURRENT
		WHERE NOT (pre.LAST_NAME <=> cur.LAST_NAME) AND pre.DATE_INSERTED = @DATE_INSERTED_PREVIOUS) AS LastName
		ON FirstName.DATAID = LastName.DATAID 
		    

		LEFT JOIN (
			SELECT pre.DATAID,
			    pre.SDN_TYPE AS PREVIOUS_SDN_TYPE,
			    cur.SDN_TYPE AS CURRENT_SDN_TYPE
			FROM ofac_sdn pre
			    LEFT JOIN ofac_sdn cur
			    ON cur.DATAID = pre.DATAID
			    AND cur.DATE_INSERTED = @DATE_INSERTED_CURRENT
			WHERE NOT (pre.SDN_TYPE <=> cur.SDN_TYPE) AND pre.DATE_INSERTED = @DATE_INSERTED_PREVIOUS) AS SDN_TYPE1
		    ON FirstName.DATAID = SDN_TYPE1.DATAID
		    
		
		  
		LEFT JOIN (
			SELECT pre.DATAID,
			    pre.REMARKS AS PREVIOUS_REMARKS,
			    cur.REMARKS AS CURRENT_REMARKS
			FROM ofac_sdn pre
			    LEFT JOIN ofac_sdn cur
			    ON cur.DATAID = pre.DATAID
			    AND cur.DATE_INSERTED = @DATE_INSERTED_CURRENT
			WHERE NOT (pre.REMARKS <=> cur.REMARKS) AND pre.DATE_INSERTED = @DATE_INSERTED_PREVIOUS) AS REMARKS1
		    ON FirstName.DATAID = REMARKS1.DATAID   
		
		LEFT JOIN (
			SELECT pre.DATAID,
			    pre.PROGRAM_LIST AS PREVIOUS_PROGRAM_LIST,
			    cur.PROGRAM_LIST AS CURRENT_PROGRAM_LIST
			FROM ofac_sdn pre
			    LEFT JOIN ofac_sdn cur
			    ON cur.DATAID = pre.DATAID
			    AND cur.DATE_INSERTED = @DATE_INSERTED_CURRENT
			WHERE NOT (pre.PROGRAM_LIST <=> cur.PROGRAM_LIST) AND pre.DATE_INSERTED = @DATE_INSERTED_PREVIOUS) AS PROGRAM_LIST1
		    ON FirstName.DATAID = PROGRAM_LIST1.DATAID
  
			  
	    )     
	    GROUP BY FirstName.DATAID
		HAVING FirstName.DATAID = l.DATAID
		),
	    '</DATAID>') AS xmldoc
	FROM tmp_ofac l;
	
	BEGIN
	UPDATE compliance.ofac_sdn AS A
	INNER JOIN compliance.tmp2_ofac_sdn AS B
		ON A.DATAID = B.DATAID
	SET A.xml_col = B.xmldoc	
	WHERE B.xmldoc IS NOT NULL
	AND A.DATE_INSERTED = DATE_FORMAT(STR_TO_DATE(@DATE_INSERTED_CURRENT, '%Y-%m-%d %H:%i'),'%Y-%m-%d %H:%i');
	END;	
  END
  //
DELIMITER ;