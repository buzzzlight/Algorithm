-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS 
LEFT JOIN ANIMAL_INS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID WHERE ANIMAL_INS.ANIMAL_ID IS NULL;