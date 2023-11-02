-- 코드를 입력하세요
SELECT
    R.REST_ID
    , I.REST_NAME
    , I.FOOD_TYPE
    , I.FAVORITES
    , I.ADDRESS
    , ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW AS R
JOIN REST_INFO AS I
ON R.REST_ID = I.REST_ID
GROUP BY R.REST_ID HAVING I.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, I.FAVORITES DESC