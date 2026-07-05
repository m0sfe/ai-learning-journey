def show_skill_report(skills: list[dict]) -> None:
    print("AI Learning Progress Report")
    print("-" * 35)

    for skill in skills:
        name = skill["name"]
        level = skill["level"]
        focus = skill["focus"]

        print(f"Skill: {name}")
        print(f"Current Level: {level}/5")
        print(f"Current Focus: {focus}")
        print("-" * 35)


if __name__ == "__main__":
    my_skills = [
        {
            "name": "Python Functions",
            "level": 2,
            "focus": "Writing reusable functions"
        },
        {
            "name": "Git and GitHub",
            "level": 1,
            "focus": "Committing and pushing projects"
        },
        {
            "name": "Data Science Project Structure",
            "level": 1,
            "focus": "Organizing files for portfolio projects"
        }
    ]

    show_skill_report(my_skills)