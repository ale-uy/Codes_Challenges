SELECT
CASE
    WHEN Grade >= 8 
    THEN Name
    ELSE NULL
END Name, Grade, Marks
FROM Students JOIN Grades ON Marks BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade DESC, name;