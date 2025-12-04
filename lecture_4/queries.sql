-- 3. Все оценки Alice Johnson
SELECT subject, grade
FROM grades
WHERE student_id = (SELECT id FROM students WHERE full_name = 'Alice Johnson');

-- 4. Средний балл каждого студента
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC;

-- 5. Студенты после 2004 года
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year DESC;

-- 6. Средний балл по предметам
SELECT subject, ROUND(AVG(grade), 2) AS avg_subject_grade, COUNT(*) AS count
FROM grades
GROUP BY subject
ORDER BY avg_subject_grade DESC;

-- 7. Топ-3 студентов по среднему баллу
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- 8. Студенты с хотя бы одной оценкой ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name;