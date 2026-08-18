#학생-과목-수강 관계 JOIN
SELECT 
    s.student_id,
    s.name AS student_name,
    sub.subject_name,
    e.enrolled_date
FROM Enrollment e
JOIN Student s ON e.student_id = s.student_id
JOIN Subject sub ON e.subject_id = sub.subject_id
ORDER BY s.student_id;

#학생-학부모 관계 JOIN
SELECT 
    s.student_id,
    s.name AS student_name,
    p.name AS parent_name,
    p.relation_type
FROM Student s
LEFT JOIN Parent p ON s.student_id = p.student_id
ORDER BY s.student_id;

#학생-멘토-상담 관계 JOIN(가장 복합적)
SELECT 
    s.name AS student_name,
    t.name AS tutor_name,
    c.category AS consultation_type,
    c.date AS consultation_daStudentte
FROM Consultation c
JOIN Student s ON c.student_id = s.student_id
JOIN Tutor t ON c.tutor_id = t.tutor_id
ORDER BY c.date;
