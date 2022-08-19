# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class ActiveLearningScoreData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'MongoObjectID',
        'tag_id': 'MongoObjectID',
        'score_type': 'ActiveLearningScoreType',
        'scores': 'ActiveLearningScores',
        'created_at': 'Timestamp'
    }

    attribute_map = {
        'id': 'id',
        'tag_id': 'tagId',
        'score_type': 'scoreType',
        'scores': 'scores',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, tag_id=None, score_type=None, scores=None, created_at=None, _configuration=None):  # noqa: E501
        """ActiveLearningScoreData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._tag_id = None
        self._score_type = None
        self._scores = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.tag_id = tag_id
        self.score_type = score_type
        self.scores = scores
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this ActiveLearningScoreData.  # noqa: E501


        :return: The id of this ActiveLearningScoreData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActiveLearningScoreData.


        :param id: The id of this ActiveLearningScoreData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tag_id(self):
        """Gets the tag_id of this ActiveLearningScoreData.  # noqa: E501


        :return: The tag_id of this ActiveLearningScoreData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ActiveLearningScoreData.


        :param tag_id: The tag_id of this ActiveLearningScoreData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and tag_id is None:
            raise ValueError("Invalid value for `tag_id`, must not be `None`")  # noqa: E501

        self._tag_id = tag_id

    @property
    def score_type(self):
        """Gets the score_type of this ActiveLearningScoreData.  # noqa: E501


        :return: The score_type of this ActiveLearningScoreData.  # noqa: E501
        :rtype: ActiveLearningScoreType
        """
        return self._score_type

    @score_type.setter
    def score_type(self, score_type):
        """Sets the score_type of this ActiveLearningScoreData.


        :param score_type: The score_type of this ActiveLearningScoreData.  # noqa: E501
        :type: ActiveLearningScoreType
        """
        if self._configuration.client_side_validation and score_type is None:
            raise ValueError("Invalid value for `score_type`, must not be `None`")  # noqa: E501

        self._score_type = score_type

    @property
    def scores(self):
        """Gets the scores of this ActiveLearningScoreData.  # noqa: E501


        :return: The scores of this ActiveLearningScoreData.  # noqa: E501
        :rtype: ActiveLearningScores
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this ActiveLearningScoreData.


        :param scores: The scores of this ActiveLearningScoreData.  # noqa: E501
        :type: ActiveLearningScores
        """
        if self._configuration.client_side_validation and scores is None:
            raise ValueError("Invalid value for `scores`, must not be `None`")  # noqa: E501

        self._scores = scores

    @property
    def created_at(self):
        """Gets the created_at of this ActiveLearningScoreData.  # noqa: E501


        :return: The created_at of this ActiveLearningScoreData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ActiveLearningScoreData.


        :param created_at: The created_at of this ActiveLearningScoreData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ActiveLearningScoreData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActiveLearningScoreData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActiveLearningScoreData):
            return True

        return self.to_dict() != other.to_dict()