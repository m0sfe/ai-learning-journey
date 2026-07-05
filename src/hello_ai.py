def introduce(name: str, goal: str) -> str:
    return f"Hello, my name is {name}. I am learning AI to {goal}."


if __name__ == "__main__":
    message = introduce(
        name="Mohammad",
        goal="build real-world AI and Data Science projects"
    )
    print(message)