# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SubtitleDataDetail(object):
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
        'season_number': 'int',
        'id': 'str',
        'rate': 'str',
        'title': 'str',
        'owner': 'str',
        'comment': 'str',
        'link': 'str'
    }

    attribute_map = {
        'season_number': 'seasonNumber',
        'id': 'id',
        'rate': 'rate',
        'title': 'title',
        'owner': 'owner',
        'comment': 'comment',
        'link': 'link'
    }

    def __init__(self, season_number=None, id=None, rate=None, title=None, owner=None, comment=None, link=None):  # noqa: E501
        """SubtitleDataDetail - a model defined in Swagger"""  # noqa: E501
        self._season_number = None
        self._id = None
        self._rate = None
        self._title = None
        self._owner = None
        self._comment = None
        self._link = None
        self.discriminator = None
        if season_number is not None:
            self.season_number = season_number
        if id is not None:
            self.id = id
        if rate is not None:
            self.rate = rate
        if title is not None:
            self.title = title
        if owner is not None:
            self.owner = owner
        if comment is not None:
            self.comment = comment
        if link is not None:
            self.link = link

    @property
    def season_number(self):
        """Gets the season_number of this SubtitleDataDetail.  # noqa: E501


        :return: The season_number of this SubtitleDataDetail.  # noqa: E501
        :rtype: int
        """
        return self._season_number

    @season_number.setter
    def season_number(self, season_number):
        """Sets the season_number of this SubtitleDataDetail.


        :param season_number: The season_number of this SubtitleDataDetail.  # noqa: E501
        :type: int
        """

        self._season_number = season_number

    @property
    def id(self):
        """Gets the id of this SubtitleDataDetail.  # noqa: E501


        :return: The id of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubtitleDataDetail.


        :param id: The id of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rate(self):
        """Gets the rate of this SubtitleDataDetail.  # noqa: E501


        :return: The rate of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this SubtitleDataDetail.


        :param rate: The rate of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def title(self):
        """Gets the title of this SubtitleDataDetail.  # noqa: E501


        :return: The title of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SubtitleDataDetail.


        :param title: The title of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def owner(self):
        """Gets the owner of this SubtitleDataDetail.  # noqa: E501


        :return: The owner of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SubtitleDataDetail.


        :param owner: The owner of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def comment(self):
        """Gets the comment of this SubtitleDataDetail.  # noqa: E501


        :return: The comment of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SubtitleDataDetail.


        :param comment: The comment of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def link(self):
        """Gets the link of this SubtitleDataDetail.  # noqa: E501


        :return: The link of this SubtitleDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SubtitleDataDetail.


        :param link: The link of this SubtitleDataDetail.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if issubclass(SubtitleDataDetail, dict):
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
        if not isinstance(other, SubtitleDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
