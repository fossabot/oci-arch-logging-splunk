# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Disk(object):
    """
    The assets disk.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Disk object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Disk.
        :type name: str

        :param boot_order:
            The value to assign to the boot_order property of this Disk.
        :type boot_order: int

        :param uuid:
            The value to assign to the uuid property of this Disk.
        :type uuid: str

        :param uuid_lun:
            The value to assign to the uuid_lun property of this Disk.
        :type uuid_lun: str

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this Disk.
        :type size_in_mbs: int

        :param location:
            The value to assign to the location property of this Disk.
        :type location: str

        :param persistent_mode:
            The value to assign to the persistent_mode property of this Disk.
        :type persistent_mode: str

        """
        self.swagger_types = {
            'name': 'str',
            'boot_order': 'int',
            'uuid': 'str',
            'uuid_lun': 'str',
            'size_in_mbs': 'int',
            'location': 'str',
            'persistent_mode': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'boot_order': 'bootOrder',
            'uuid': 'uuid',
            'uuid_lun': 'uuidLun',
            'size_in_mbs': 'sizeInMBs',
            'location': 'location',
            'persistent_mode': 'persistentMode'
        }

        self._name = None
        self._boot_order = None
        self._uuid = None
        self._uuid_lun = None
        self._size_in_mbs = None
        self._location = None
        self._persistent_mode = None

    @property
    def name(self):
        """
        Gets the name of this Disk.
        Disk name.


        :return: The name of this Disk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Disk.
        Disk name.


        :param name: The name of this Disk.
        :type: str
        """
        self._name = name

    @property
    def boot_order(self):
        """
        Gets the boot_order of this Disk.
        Order of boot volumes.


        :return: The boot_order of this Disk.
        :rtype: int
        """
        return self._boot_order

    @boot_order.setter
    def boot_order(self, boot_order):
        """
        Sets the boot_order of this Disk.
        Order of boot volumes.


        :param boot_order: The boot_order of this Disk.
        :type: int
        """
        self._boot_order = boot_order

    @property
    def uuid(self):
        """
        Gets the uuid of this Disk.
        Disk UUID for the virtual disk, if available.


        :return: The uuid of this Disk.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this Disk.
        Disk UUID for the virtual disk, if available.


        :param uuid: The uuid of this Disk.
        :type: str
        """
        self._uuid = uuid

    @property
    def uuid_lun(self):
        """
        Gets the uuid_lun of this Disk.
        Disk UUID LUN for the virtual disk, if available.


        :return: The uuid_lun of this Disk.
        :rtype: str
        """
        return self._uuid_lun

    @uuid_lun.setter
    def uuid_lun(self, uuid_lun):
        """
        Sets the uuid_lun of this Disk.
        Disk UUID LUN for the virtual disk, if available.


        :param uuid_lun: The uuid_lun of this Disk.
        :type: str
        """
        self._uuid_lun = uuid_lun

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this Disk.
        The size of the volume in MBs.


        :return: The size_in_mbs of this Disk.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this Disk.
        The size of the volume in MBs.


        :param size_in_mbs: The size_in_mbs of this Disk.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def location(self):
        """
        Gets the location of this Disk.
        Location of the boot/data volume.


        :return: The location of this Disk.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Disk.
        Location of the boot/data volume.


        :param location: The location of this Disk.
        :type: str
        """
        self._location = location

    @property
    def persistent_mode(self):
        """
        Gets the persistent_mode of this Disk.
        The disk persistent mode.


        :return: The persistent_mode of this Disk.
        :rtype: str
        """
        return self._persistent_mode

    @persistent_mode.setter
    def persistent_mode(self, persistent_mode):
        """
        Sets the persistent_mode of this Disk.
        The disk persistent mode.


        :param persistent_mode: The persistent_mode of this Disk.
        :type: str
        """
        self._persistent_mode = persistent_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
