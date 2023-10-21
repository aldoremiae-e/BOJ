-- 회원별 리뷰의 수가 MAX인 회원의 리뷰를 찾아야해
SELECT
    P.MEMBER_NAME
    , R.REVIEW_TEXT
    , DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS P
JOIN REST_REVIEW AS R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID IN
(SELECT
    MEMBER_ID
FROM REST_REVIEW
GROUP BY MEMBER_ID
HAVING COUNT(REVIEW_TEXT) = 
(SELECT
    COUNT(REVIEW_TEXT)
FROM REST_REVIEW AS R
GROUP BY MEMBER_ID
ORDER BY COUNT(REVIEW_TEXT) DESC
LIMIT 1))
ORDER BY R.REVIEW_DATE ASC, R.REVIEW_TEXT ASC