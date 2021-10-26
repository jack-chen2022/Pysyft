# stdlib
from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

# third party
from sqlalchemy.engine import Engine

# relative
from ..... import serialize
from ...abstract.node import AbstractNodeClient
from ...domain.enums import RequestAPIFields
from ..exceptions import AssociationRequestError
from ..node_table.association import Association
from ..node_table.association_request import AssociationRequest
from .database_manager import DatabaseManager


class AssociationRequestManager(DatabaseManager):

    schema = AssociationRequest

    def __init__(self, database: Engine) -> None:
        super().__init__(schema=AssociationRequestManager.schema, db=database)

    def first(self, **kwargs: Any) -> AssociationRequest:
        result = super().first(**kwargs)
        if not result:
            raise AssociationRequestError

        return result

    def create_association_request(
        self,
        node: str,
        source: AbstractNodeClient,
        target: AbstractNodeClient,
        metadata: Dict[str, Any],
        status: str,
        address: str,
    ) -> None:
        table_fields = {}
        table_fields[RequestAPIFields.NODE] = node
        table_fields[RequestAPIFields.REQUESTED_DATE] = datetime.now().strftime(
            "%m/%d/%Y"
        )

        source_blob = serialize(source, to_bytes=True)
        target_blob = serialize(target, to_bytes=True)

        table_fields[RequestAPIFields.SOURCE] = source_blob  # type: ignore
        table_fields[RequestAPIFields.TARGET] = target_blob  # type: ignore
        table_fields[RequestAPIFields.STATUS] = status
        table_fields[RequestAPIFields.ADDRESS] = address

        if super().first(address=address):
            self.modify(query={"address": address}, values=table_fields)
        else:
            self.register(**table_fields)  # type: ignore

    # def associations(self) -> List[Association]:
    #     return list(self.db.session.query(Association).all())

    def association(self, **kwargs: Dict[str, Any]) -> Optional[Association]:
        return self.db.session.query(Association).filter_by(**kwargs).first()

    def set(self, address: str, response: str) -> None:
        self.modify(
            {"address": address},
            {"status": response, "accepted_date": datetime.now().strftime("%m/%d/%Y")},
        )
