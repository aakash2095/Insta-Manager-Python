class Post:
    post_list = []
    next_post_id = 1

    def __init__(self, user, content):
        self.post_id = Post.next_post_id
        Post.next_post_id += 1
        self.user = user
        self.content = content
        self.likes = 0

    def add_post(self):
        Post.post_list.append(self)

    def show(self):
        print(f"Post ID: {self.post_id}")
        print(f"User: {self.user}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")
        print("-" * 40)

    @classmethod
    def get_post_list(cls):
        return cls.post_list

    @classmethod
    def update_post(cls, post_id, new_content):
        for post in cls.post_list:
            if post.post_id == post_id:
                post.content = new_content
                return True
        return False

    @classmethod
    def delete_post(cls, post_id):
        for post in cls.post_list:
            if post.post_id == post_id:
                cls.post_list.remove(post)
                return True
        return False

    @classmethod
    def search_post(cls, post_id):
        for post in cls.post_list:
            if post.post_id == post_id:
                return post
        return None

    def like_post(self):
        self.likes += 1


def main():
    while True:
        print("\nWelcome to Insta Post Manager!")
        print("1. Add Post")
        print("2. Show All Posts")
        print("3. Update Post")
        print("4. Delete Post")
        print("5. Search Post")
        print("6. Like Post")
        print("7. Exit")

        choice = input("Select an option from 1-7: ")

        if choice == "1":
            user = input("Enter Username: ")
            content = input("Enter Post Content: ")
            new_post = Post(user, content)
            new_post.add_post()
            print("Post added successfully!")

        elif choice == "2":
            if Post.get_post_list():
                for post in Post.get_post_list():
                    post.show()
            else:
                print("No posts available.")

        elif choice == "3":
            post_id = int(input("Enter Post ID to update: "))
            new_content = input("Enter new content: ")
            if Post.update_post(post_id, new_content):
                print("Post updated successfully!")
            else:
                print("Post not found.")

        elif choice == "4":
            post_id = int(input("Enter Post ID to delete: "))
            if Post.delete_post(post_id):
                print("Post deleted successfully!")
            else:
                print("Post not found.")

        elif choice == "5":
            post_id = int(input("Enter Post ID to search: "))
            post = Post.search_post(post_id)
            if post:
                post.show()
            else:
                print("Post not found.")

        elif choice == "6":
            post_id = int(input("Enter Post ID to like: "))
            post = Post.search_post(post_id)
            if post:
                post.like_post()
                print("You liked the post!")
            else:
                print("Post not found.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 7.")


if __name__ == "__main__":
    main()
