import  itertools

class BaseStore():

    def __init__(self,data_provider,last_id):
        self._data_provider = data_provider
        self._last_id = last_id


    def get_all(self):
        return self._data_provider


    def add(self,item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self.last_id += 1


    def get_by_id(self,id):
        all_item_instance = self.get_all()
        for item_instance in all_item_instance:
            if item_instance.id == id:
                return item_instance


    def update(self,instance):
        result = instance
        all_instance = self.get_all()

        for index, current_instance in enumerate(all_instance):
            if current_instance.id == instance.id:
                all_instance[index] = instance
                break

        return result

    def delete(self,id):
      instance = self.get_by_id(id)
      self._data_provider.remove(instance)

    def entity_exists(self,item_instance):
        if self.get_by_id(item_instance.id):
            return True
        return False

class MemberStore(BaseStore):

    members = []
    last_id = 1


    def __init__(self):
        BaseStore.__init__(self,MemberStore.members,MemberStore.last_id)


    def get_by_name(self, member_name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, all_posts):
            if member.id is post.member_id:
                member.posts.append(post)
        for member in all_members:
            yield member

    def get_top_two(self, post_store):
        all_members = self.get_members_with_posts(post_store)
        all_members = sorted(all_members, key=lambda x: len(x.posts), reverse=True)
        return all_members[:2]


class PostStore(BaseStore):

    posts = []
    last_id = 1


    def __init__(self):
        BaseStore.__init__(self,PostStore.posts,PostStore.last_id)



    def get_posts_by_date(self):
        all_posts = self.get_all()
        posts_sorted_bydate = sorted(all_posts, key=lambda post: post.date)
        return posts_sorted_bydate
