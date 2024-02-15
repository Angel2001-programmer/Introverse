from flask_restx import Resource, Namespace, fields
from flask import request
from models.forum_models import Message
from flask_jwt_extended import get_jwt_identity, jwt_required

forum_ns = Namespace("forum", description="A namespace for the message board.")

message_model = forum_ns.model("Message", {
    "post_id": fields.Integer(description="ID"),
    "post_content": fields.String(description="Text content of the message"),
    "post_category": fields.String(description="Category of the message"),
    "post_author": fields.String(description="Author of the message"),
    "post_date": fields.DateTime(description="Time and date message was posted", dt_format='rfc822')
})


@forum_ns.route("/all")
class ForumResource(Resource):
    @forum_ns.marshal_list_with(message_model)
    def get(self):
        """Get all messages"""
        messages = Message.query.all()
        return messages
    
    @forum_ns.marshal_with(message_model)
    @forum_ns.expect(message_model)
    @jwt_required()
    def post(self):
        """Create a new message"""
        data = request.get_json()
        new_post = Message(
            post_content = data.get("post_content"),
            post_category = data.get("post_category"),
            post_author = data.get("post_author"),
            post_date = data.get("post_date")
        )

        new_post.create()

        return new_post, 201


@forum_ns.route("/id/<int:id>")
class ForumIdResource(Resource):

    @forum_ns.marshal_with(message_model)
    def get(self, id):
        """Get message by id"""
        result = Message.query.get_or_404(id)

        return result
    
    # @forum_ns.marshal_with(message_model)
    # @jwt_required()  # Need to test if it works on frontend
    # def put(self, id):
    #     """Update a message by id"""
    #     username=get_jwt_identity()
    #     edit_message = Message.query.filter(Message.post_id == id, Message.post_author == username).first()

    #     data = request.get_json()

    #     edit_message.update(data.get("post_content"))

    #     return edit_message
    
    @forum_ns.marshal_with(message_model)
    # @jwt_required()  # This route used for testing in Postman, delete it and uncomment other route
    def put(self, id):
        """Update a message by id"""
        edit_message = Message.query.filter(Message.post_id == id).first()

        data = request.get_json()

        edit_message.update(data.get("post_content"))

        return edit_message
    
    @forum_ns.marshal_with(message_model)
    @jwt_required()  # This will not work currently, need to solve jwt required and identity issue
    def delete(self, id):
        """Delete a message by id"""
        username=get_jwt_identity()
        delete_message = Message.query.filter(Message.post_id == id, Message.post_author == username).first()

        delete_message.delete()

        return delete_message


@forum_ns.route("/category/<string:category>")
class ForumCatResource(Resource):

    @forum_ns.marshal_list_with(message_model)
    def get(self, category):
        """Get messages by category"""
        result = Message.query.filter(Message.post_category == category).all()

        return result
    

@forum_ns.route("/author/<string:author>")
class ForumAuthorResource(Resource):

    @forum_ns.marshal_list_with(message_model)
    def get(self, author):
        """Get messages by author username"""
        result = Message.query.filter(Message.post_author == author).all()

        return result
    