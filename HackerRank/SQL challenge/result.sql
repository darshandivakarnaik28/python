select h.hacker_id,h.name,
count(s.challenge_id) as a from 
Hackers h JOIN Challenges s ON h.hacker_id=s.hacker_id
group by h.hacker_id,h.name

HAVING count(s.challenge_id)=
(SELECT MAX(challenge_count) FROM (SELECT COUNT(challenge_id ) as challenge_count FROM Challenges
GROUP BY hacker_id)s1)
OR
count(s.challenge_id) in (SELECT challenge_count FROM(SELECT hacker_id,COUNT(challenge_id) AS challenge_count from Challenges
group by hacker_id)s2
group by challenge_count
having count(hacker_id)=1)

order by a DESC,h.hacker_id ASC;
