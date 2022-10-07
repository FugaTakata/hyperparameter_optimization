from quality_metrics import angular_resolution, \
    aspect_ratio, \
    crossing_angle_maximization, \
    crossing_number,\
    gabriel_graph_property,\
    ideal_edge_length, \
    node_resolution, \
    shape_based_metrics, \
    stress
from utils import edge_crossing_finder


def calc_quality_metrics(nx_graph, pos):
    edge_crossing = edge_crossing_finder(nx_graph, pos)

    quality_metrics = {}
    quality_metrics['angular_resolution'] = angular_resolution(nx_graph, pos)
    quality_metrics['aspect_ratio'] = aspect_ratio(pos)
    quality_metrics['crossing_angle_maximization'] = crossing_angle_maximization(
        nx_graph, pos, edge_crossing)
    quality_metrics['crossing_number'] = crossing_number(
        nx_graph, pos, edge_crossing)
    quality_metrics['gabriel_graph_property'] = gabriel_graph_property(
        nx_graph, pos)
    quality_metrics['ideal_edge_length'] = ideal_edge_length(nx_graph, pos)
    quality_metrics['node_resolution'] = node_resolution(pos)
    quality_metrics['shape_based_metrics'] = shape_based_metrics(nx_graph, pos)
    quality_metrics['stress'] = stress(nx_graph, pos)

    return quality_metrics
