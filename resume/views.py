from django.shortcuts import render

def cv_view(request):
    # Sample data - replace these with actual data
    education_list = [
        {"degree": "MSc Computer Science", "institution": "New York University", "graduation_year": 2026, "details": "Notable courses: Notable courses: Machine Learning; Design and Analysis of Algorithms; Internet, Security and Privacy."},
        {"degree": "BTech Information Technology", "institution": "National Institute of Technology Karnataka", "graduation_year": 2023, "details": "Notable courses: Object-Oriented Programming, Operating Systems, Data Structures and Algorithms, Software Development; Operating Systems; Computer Architecture; Data Science; Machine Learning; Deep Learning; Natural Language Processing; Computer Vision; Android Development; Computer Networking."},
    ]
    
    work_experience = [
        {"position": "Software Engineer", "company": "Citicorp Services Bangalore, India", "start_date": "2023-07-01", "end_date": "2024-08-01", "description": "Implemented Java functionality to flag incorrect certificates, preventing start-up errors and pod crashes in production. Developed Macros functionality to automate the collection of employee data reducing manual individual effort by 20 hours a week. Designed and implemented  robust functionality within the Core API Framework for digital applications using Java, Spring, and Tomcat; improved system response time by 40% through optimized code structures."},
        {"position": "Intern", "company": "Royal Bank of Scotland Bangalore, India", "start_date": "2022-05-01", "end_date": "2021-07-31", "description": "Developed an interactive dashboard using Salesforce that visualized key metrics from user behavior analysis; findings directly led to targeted marketing strategies to increase client interaction by 30%. Dashboard depicted client interest and behavior, helping to cater services according to these preferences to high-value customers"},
    ]
    
    research_work = [
        {"title": "The Effect of Sampling in the Machine Learning-based Malware Analysis", "journal": "Springer Book Series, 'Algorithms for Intelligent Systems ( AIS )'", "year": 2021},
    ]
    
    publications = [
        {"title": "Online Video Stabilization using Mesh Flow with Minimum Latency", "journal": "IEEE International Conference in the Proceedings ‘2023 IEEE International Conference on Industry 4.0, Artificial Intelligence, and Communications Technology ( IAICT )’", "year": 2023},
    ]
    
    skills = ["Python", "Django", "Machine Learning", "HTML/CSS","Java", "SǪL", "C++", "C", "JavaScript"]
    certifications = ["Machine Learning Bootcamp", "Android Development Bootcamp and Internet of Things Bootcamp at IIT Bombay, India","Ethical Hacking","Neural Networks and Deep Learning"]
    achievements = ["State Level National Talent Search Examination Awardee for 2016-2017 with a scholarship for Higher Secondary studies by the Department of State Educational Research and Training (DSERT), Bengaluru, Karnataka, India"]

    context = {
        'education_list': education_list,
        'work_experience': work_experience,
        'research_work': research_work,
        'publications': publications,
        'skills': skills,
        'certifications': certifications,
        'achievements': achievements,
    }

    return render(request, 'resume/cv.html', context)
