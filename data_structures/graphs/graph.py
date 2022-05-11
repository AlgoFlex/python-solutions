from __future__ import annotations
from typing import List, Generic, TypeVar
from data_structures.node import GraphNode

T = TypeVar("T")


class Graph(Generic[T]):
    def __init__(self, vertices: List[GraphNode]) -> None:
        self.__vertices = vertices

    @property
    def vertices(self) -> List[GraphNode]:
        return self.__vertices

    def add_edge(self, vertex1: GraphNode, vertex2: GraphNode) -> None:
        if vertex1 in self.__vertices and vertex2 in self.__vertices:
            vertex1.add_child(vertex2)
            vertex2.add_child(vertex1)

    def remove_edge(self, vertex1: GraphNode, vertex2: GraphNode) -> None:
        if vertex1 in self.__vertices and vertex2 in self.__vertices:
            vertex1.remove_child(vertex2)
            vertex2.remove_child(vertex1)
