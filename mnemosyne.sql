UPDATE cards
    SET answer = substr(answer, 4, instr(answer, '?') - 4),
    SET question = substr(question, instr(question, '<img'))
    WHERE tags LIKE '%africa%' and instr(answer, '?') > 0;

UPDATE cards
    SET question = substr(question, 4, instr(question, '?') - 4),
    SET answer = substr(answer, instr(answer, '<img'))
    WHERE tags LIKE '%africa%' and instr(question, '?') > 0;