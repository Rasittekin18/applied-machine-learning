import pandas as pd
import random
import os

ROLES_DATA = {
    "Data Science & AI": {
        "titles": [
            "Data Scientist", "Machine Learning Engineer", "AI Researcher",
            "Data Analyst", "NLP Engineer", "Computer Vision Specialist", "Deep Learning Engineer"
        ],
        "core_skills": [
            "Python", "SQL", "Pandas", "NumPy", "Scikit-Learn", "Machine Learning",
            "Data Analysis", "Feature Engineering", "Statistics"
        ],
        "advanced_skills": [
            "PyTorch", "TensorFlow", "Deep Learning", "NLP", "Computer Vision",
            "Transformers", "XGBoost", "MLOps", "Big Data", "Spark", "Recommendation Systems"
        ],
        "tasks": [
            "developing predictive machine learning models and pipelines",
            "conducting exploratory data analysis and statistical modeling",
            "optimizing deep learning architectures for production deployment",
            "building end-to-end NLP and text classification systems",
            "collaborating with cross-functional teams to deliver data-driven insights",
            "designing A/B tests and evaluating model performance metrics like F1-score and ROC-AUC"
        ]
    },
    "Backend Development": {
        "titles": [
            "Backend Developer", "Software Engineer (Backend)", "API Developer",
            "Java Software Engineer", "Python Backend Engineer", ".NET Developer", "Golang Engineer"
        ],
        "core_skills": [
            "Python", "Java", "C#", "SQL", "PostgreSQL", "REST API", "Git", "OOP", "Relational Databases"
        ],
        "advanced_skills": [
            "FastAPI", "Django", "Spring Boot", "Microservices", "Docker", "Kubernetes",
            "Redis", "Kafka", "RabbitMQ", "GraphQL", "gRPC", "MongoDB"
        ],
        "tasks": [
            "designing and implementing scalable RESTful APIs and microservices",
            "optimizing relational and NoSQL database queries for high throughput",
            "building asynchronous event-driven pipelines using message brokers",
            "implementing robust authentication, authorization, and security protocols",
            "writing unit and integration tests to ensure code reliability",
            "collaborating with frontend developers to define efficient API contracts"
        ]
    },
    "Frontend Development": {
        "titles": [
            "Frontend Developer", "React Developer", "UI Engineer",
            "Vue.js Developer", "Web Application Developer", "JavaScript/TypeScript Engineer"
        ],
        "core_skills": [
            "JavaScript", "TypeScript", "HTML5", "CSS3", "React", "Git", "Responsive Design"
        ],
        "advanced_skills": [
            "Next.js", "Vue.js", "Angular", "Redux", "Tailwind CSS", "Sass",
            "Webpack", "Vite", "UI/UX", "Jest", "Cypress", "Web Performance"
        ],
        "tasks": [
            "developing modern, responsive, and interactive user interfaces",
            "integrating RESTful and GraphQL APIs with frontend client state",
            "optimizing web applications for maximum speed, accessibility, and scalability",
            "building reusable component libraries using React and Tailwind CSS",
            "writing frontend unit and end-to-end tests using Jest and Cypress",
            "working closely with UI/UX designers to translate Figma mockups into code"
        ]
    },
    "DevOps & Cloud": {
        "titles": [
            "DevOps Engineer", "Cloud Infrastructure Engineer", "Site Reliability Engineer (SRE)",
            "Platform Engineer", "Kubernetes Specialist", "Cloud Architect"
        ],
        "core_skills": [
            "Linux", "Docker", "Git", "Bash", "Networking", "CI/CD Pipelines"
        ],
        "advanced_skills": [
            "Kubernetes", "AWS", "Azure", "GCP", "Terraform", "Ansible",
            "Jenkins", "GitHub Actions", "Prometheus", "Grafana", "Nginx", "Helm"
        ],
        "tasks": [
            "automating continuous integration and continuous deployment (CI/CD) pipelines",
            "provisioning and maintaining multi-cloud infrastructure using Terraform (IaC)",
            "managing containerized workloads and cluster scaling on Kubernetes",
            "setting up comprehensive monitoring, logging, and alerting with Prometheus and Grafana",
            "ensuring high availability, fault tolerance, and cloud infrastructure security",
            "troubleshooting complex production environment issues and optimizing cloud costs"
        ]
    }
}

LEVEL_PROFILES = {
    "Junior": {
        "exp_phrases": [
            "0-2 years of relevant software development experience",
            "Entry-level or recent graduate with strong passion for technology",
            "1+ year of hands-on internship or project experience",
            "Demonstrated foundational understanding through personal projects and coursework"
        ],
        "prefixes": ["Junior", "Associate", "Entry-Level", ""]
    },
    "Mid": {
        "exp_phrases": [
            "3-5 years of professional software engineering experience",
            "Proven track record of delivering production-grade software solutions",
            "Strong familiarity with modern architectural design patterns and best practices",
            "Solid experience working autonomously and collaborating within agile scrum teams"
        ],
        "prefixes": ["Mid-Level", "", "Experienced"]
    },
    "Senior": {
        "exp_phrases": [
            "5+ years of extensive industry experience leading technical initiatives",
            "Demonstrated leadership in designing large-scale distributed architectures",
            "Proven ability to mentor junior engineers and drive best engineering practices",
            "Extensive experience in system architecture, performance optimization, and tech strategy"
        ],
        "prefixes": ["Senior", "Lead", "Principal", "Staff"]
    }
}

def generate_job_postings(num_samples=720):
    records = []
    
    for _ in range(num_samples):
        role_name = random.choice(list(ROLES_DATA.keys()))
        level_name = random.choice(list(LEVEL_PROFILES.keys()))
        
        role_info = ROLES_DATA[role_name]
        level_info = LEVEL_PROFILES[level_name]
        
        prefix = random.choice(level_info["prefixes"])
        base_title = random.choice(role_info["titles"])
        title = f"{prefix} {base_title}".strip()
        
        exp_phrase = random.choice(level_info["exp_phrases"])
        
        # Skill selection based on seniority
        num_core = random.randint(3, len(role_info["core_skills"]))
        chosen_core = random.sample(role_info["core_skills"], num_core)
        
        if level_name == "Junior":
            num_adv = random.randint(1, 3)
        elif level_name == "Mid":
            num_adv = random.randint(3, 5)
        else: # Senior
            num_adv = random.randint(5, min(8, len(role_info["advanced_skills"])))
        chosen_adv = random.sample(role_info["advanced_skills"], num_adv)
        
        all_skills = chosen_core + chosen_adv
        skills_str = ", ".join(all_skills)
        
        chosen_tasks = random.sample(role_info["tasks"], random.randint(3, 5))
        tasks_bullets = "\n".join([f"- Responsible for {t}." for t in chosen_tasks])
        
        description = (
            f"We are actively seeking a talented and motivated {title} to join our growing team.\n\n"
            f"Key Responsibilities:\n{tasks_bullets}\n\n"
            f"Qualifications and Requirements:\n"
            f"- {exp_phrase}.\n"
            f"- Hands-on proficiency with: {skills_str}.\n"
            f"- Strong understanding of software development life cycle, Git version control, and agile methodologies.\n"
            f"- Excellent problem solving, analytical thinking, and team communication skills."
        )
        
        records.append({
            "Title": title,
            "Role": role_name,
            "Level": level_name,
            "Skills": skills_str,
            "Description": description
        })
        
    df = pd.DataFrame(records)
    os.makedirs("JobFit_AI/data", exist_ok=True)
    df.to_csv("JobFit_AI/data/job_postings.csv", index=False, encoding="utf-8")
    print(f"Başarıyla {len(df)} adet etiketli iş ilanı oluşturuldu: JobFit_AI/data/job_postings.csv")

if __name__ == "__main__":
    generate_job_postings()

